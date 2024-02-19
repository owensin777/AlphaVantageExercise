import requests
import yaml
import json
import logging

class Analysis:
    def __init__(self, github_token, ntfy, plot_color, plot_x_title, plot_y_title, figure_size, default_save_path, function, symbol, analysis_type, api_key):
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


def Analysis(analysis_config: str):
    try:
            with open("../config/user_config.yml",'r') as yamlfile:
                user_config = yaml.safe_load(yamlfile)

            with open("../config/analysis_config.yml",'r') as yamlfile:
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
                            api_key = user_config["key"]
                            )
    
    #json.dumps({ "function": config['function'], "symbol": config['symbol'], "analysis_type" = config['analysisType']})
 
    return analysis_obj


def load_data():

 
    #except Error as e:
        
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey=' + secret['key'] 


    r = requests.get(url)
    json_content = r.json()

    json_content= json_content[analysis_type]
    
    return None


load_data()


