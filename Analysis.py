import requests
import yaml
import json
import logging
import re

class Analysis:
    def __init__(self, github_token, ntfy, plot_color, plot_x_title, plot_y_title, figure_size, default_save_path, function, symbol, analysis_type, api_key, data_type, period):
        self.github_token = github_token
        self.ntfy = ntfy
        self.plot_color = plot_color
        self.plot_x_title = plot_x_title
        self.plot_y_title = plot_y_title
        self.figure_size = figure_size
        self.default_save_path = default_save_path
        self.function = function
        self.symbol = symbol
        self.analysis_type = analysis_type
        self.api_key = api_key
        self.period = period
        self.data_type = data_type

def load_config(analysis_config: str):
    try:
            with open( analysis_config + "/user_config.yml",'r') as yamlfile:
                user_config = yaml.safe_load(yamlfile)

            with open( analysis_config + "/analysis_config.yml",'r') as yamlfile:
                analysis_config = yaml.safe_load(yamlfile)
    except FileNotFoundError as e:
            logging.error("Cant find the config files, please check the path again.")
            raise e

    
    analysis_obj = Analysis(github_token = user_config["github_token"], 
                            ntfy = analysis_config["ntfy"],
                            plot_color = analysis_config["plot_color"],
                            plot_x_title = analysis_config["plot_x_title"],
                            plot_y_title = analysis_config["plot_y_title"],
                            figure_size = analysis_config["figure_size"],
                            default_save_path = analysis_config["default_save_path"],
                            function = analysis_config["function"],
                            symbol = analysis_config["symbol"],
                            analysis_type = analysis_config["analysis_type"],
                            api_key = user_config["key"],
                            period = analysis_config["period"],
                            data_type = analysis_config["data_type"]
                            )
    
    #json.dumps({ "function": config['function'], "symbol": config['symbol'], "analysis_type" = config['analysisType']})
 
    return analysis_obj


def load_data(analysis_obj: Analysis):

 
    #except Error as e:
        
    url = f'https://www.alphavantage.co/query?function={analysis_obj.function}&symbol={analysis_obj.symbol}&apikey=' + analysis_obj.api_key 

    
    r = requests.get(url)

    if (r.status_code != 200):
         raise Exception("Http request failed. Please check.")
    #if 
    json_content = r.json()

    json_content= json_content[analysis_obj.analysis_type]
    
    return json_content

def compute_analysis(loaded_data:any, analysis_obj: Analysis):
    i = 0
    #  assert(data_type in ["open", "high"])
    if (analysis_obj.data_type not in ["open", "high", "low", "close", "volume"]):
        raise ValueError ("Your data time must be in [open, high, low, close, volume] ")
    data = []
    for k,item in loaded_data.items():
        for key in item.keys():
            if re.search(f".*{analysis_obj.data_type}.*", key):
                data.append(float(item[key]))

        i+=1
        if (i == analysis_obj.period):
            break

    proceeded_data = [f"This is the {analysis_obj.analysis_type} summary for {analysis_obj.symbol}'s {analysis_obj.data_type} in a period of {analysis_obj.period}: ",
                      f"The mean {analysis_obj.data_type} is {str(sum(data)/len(data))},", 
                      f"the maximum {analysis_obj.data_type} is {str(max(data))},", 
                      f"And the minimum {analysis_obj.data_type} is {str(min(data))}.", 
                      ]
    return proceeded_data


def notify_done(message: str):
    return

if __name__ == "__main__":
    config = load_config("./config")
    loaded_data = load_data(config)
    proceeded_data = compute_analysis(loaded_data=loaded_data, analysis_obj= config)
    
    #notify_done("It is done")


