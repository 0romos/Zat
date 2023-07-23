import sys
import os
import json
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalTrueColorFormatter
from pygments.style import Style
from pygments.token import Token


class ValidateFiles:
    """Utility class to validate and create necessary folders and files."""

    def folders():
        """
        Check if the folder '~/.config/zat' exists, and create it if it doesn't.
        """
        folder_path = os.path.expanduser("~/.config/zat")
        
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"[ZAT] - Folder '{folder_path}' created successfully.")
            except OSError as e:
                print(f"[ZAT] - Error creating folder '{folder_path}': {str(e)}")
        else:
            pass
    
    def files():
        """
        Check if 'colors.json' and 'config.json' exist inside the folder '~/.config/zat',
        create them if they don't exist, and add default content.
        """
        folder_path = os.path.expanduser("~/.config/zat")
        
        colors_json_path = os.path.join(folder_path, "colors.json")
        if not os.path.exists(colors_json_path):
            try:
                colors_data = {
                    "Token.Comment": "#66cdaa",
                    "Token.Keyword": "#449d6d",
                    "Token.Operator": "#3f9c73",
                    "Token.Name": "#66cdaa",
                    "Token.Number": "#80b48d",
                    "Token.String": "#d9faef",
                    "Token.Punctuation": "#66cdaa",
                    "Token.Text": "#66cdaa",
                    "Token.Keyword.Constant": "#66cdaa",
                    "Token.Keyword.Declaration": "#449d6d",
                    "Token.Keyword.Namespace": "#66cdaa",
                    "Token.Keyword.Type": "#449d6d",
                    "Token.Literal.Number": "#80b48d",
                    "Token.Literal.String": "#d9faef",
                    "Token.Name.Builtin": "#66cdaa",
                    "Token.Name.Function": "#66cdaa",
                    "Token.Name.Class": "#66cdaa",
                    "Token.Name.Exception": "#66cdaa",
                    "Token.Name.Decorator": "#66cdaa",
                    "Token.Operator.Word": "#3f9c73"
                }
                with open(colors_json_path, "w") as colors_file:
                    json.dump(colors_data, colors_file, indent=4)
                print(f"[ZAT] - File '{colors_json_path}' created successfully.")
            except Exception as e:
                print(f"[ZAT] - Error creating '{colors_json_path}': {str(e)}")
        else:
            pass

        config_json_path = os.path.join(folder_path, "config.json")
        if not os.path.exists(config_json_path):
            try:
                config_data = {
                    "highlight": True,
                    "line_numbers": True
                }
                with open(config_json_path, "w") as config_file:
                    json.dump(config_data, config_file, indent=4)
                print(f"[ZAT] - File '{config_json_path}' created successfully.")
            except Exception as e:
                print(f"[ZAT] - Error creating '{config_json_path}': {str(e)}")
        else:
            pass


class CustomStyle(Style):
    """
    CustomStyle class defines a custom syntax highlighting style for the code.

    Attributes:
        background_color (str): The background color for the code highlighting.
        styles (dict): A dictionary mapping Pygments tokens to their respective colors.

    Note:
        This class is designed to be used with Pygments library for syntax highlighting.
    """
   

    config_file_path = os.path.expanduser('~/.config/zat/colors.json')
    with open(config_file_path, 'r') as colors_file:
        config_data = json.load(colors_file)

    styles = {
        Token.Comment:      config_data['Token.Comment'],
        Token.Keyword:      config_data['Token.Keyword'],
        Token.Operator:     config_data['Token.Operator'],
        Token.Name:         config_data['Token.Name'],
        Token.Number:       config_data['Token.Number'],
        Token.String:       config_data['Token.String'],
        Token.Punctuation:  config_data['Token.Punctuation'],
        Token.Text:         config_data['Token.Text'],
        Token.Keyword.Constant: config_data['Token.Keyword.Constant'],
        Token.Keyword.Declaration: config_data['Token.Keyword.Declaration'],
        Token.Keyword.Namespace: config_data['Token.Keyword.Namespace'],
        Token.Keyword.Type: config_data['Token.Keyword.Type'],
        Token.Literal.Number: config_data['Token.Literal.Number'],
        Token.Literal.String: config_data['Token.Literal.String'],
        Token.Name.Builtin: config_data['Token.Name.Builtin'],
        Token.Name.Function: config_data['Token.Name.Function'],
        Token.Name.Class: config_data['Token.Name.Class'],
        Token.Name.Exception: config_data['Token.Name.Exception'],
        Token.Name.Decorator: config_data['Token.Name.Decorator'],
        Token.Operator.Word: config_data['Token.Operator.Word'],
    }


class Config:
    """
    Config class manages the configuration settings for pretty_cat.py.

    The configuration is stored in a JSON file with options for line numbers display
    and syntax highlighting.

    Attributes:
        config_path (str): The path to the configuration JSON file.

    Methods:
        __init__(self, config_path): Initializes the Config object.
        load_config(self): Loads the configuration from the JSON file.
        save_config(self): Saves the current configuration to the JSON file.
    """
    def __init__(self, config_path):
        """
        Initialize the Config object.

        Parameters:
            config_path (str): The path to the configuration JSON file.
        """
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        """
        Load the configuration from the JSON file.

        If the configuration file is not found, set default values for line_numbers and highlight.
        """
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                config_data = json.load(config_file)
                self.line_numbers = config_data.get("line_numbers", True)
                self.highlight = config_data.get("highlight", True)
        else:
            self.line_numbers = True
            self.highlight = True

    def save_config(self):
        """
        Save the current configuration to the JSON file.
        """
        config_data = {
            "line_numbers": self.line_numbers,
            "highlight": self.highlight,
        }
        with open(self.config_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)


def load_colors(colors_path):
    """
    Load custom colors for syntax highlighting from a JSON file.

    Parameters:
        colors_path (str): The path to the JSON file containing the custom colors.

    Returns:
        dict: A dictionary containing custom colors for different Pygments tokens.
              None if the file is not found or if there was an error parsing the JSON.
    """
    default_colors = {
        "Token.Comment": "#eeeeee",
        "Token.Keyword": "#858585",
        "Token.Operator": "#858585",
        "Token.Name": "#eeeeee",
        "Token.Number": "#6e6e6e",
        "Token.String": "#9d9d9d",
        "Token.Punctuation": "#eeeeee",
        "Token.Text": "#eeeeee"
    }

    if os.path.exists(colors_path):
        with open(colors_path, 'r') as colors_file:
            try:
                colors_data = json.load(colors_file)
                default_colors.update(colors_data)
                return default_colors
            except json.JSONDecodeError:
                print("Error: Invalid colors JSON file.")
    return default_colors


def pretty_cat(filename, config, colors=None):
    """
    Display the contents of a file with syntax highlighting and line numbers (optional).

    Parameters:
        filename (str): The path to the file to be displayed.
        config (Config): The Config object containing the user's configuration settings.
        colors (dict, optional): A dictionary containing custom colors for syntax highlighting.

    Note:
        This function uses Pygments library for syntax highlighting and supports various file types.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If there is an error while processing the file.
    """
    try:
        with open(filename, 'r') as file:
            code = file.read()
            lexer = get_lexer_by_name(filename.split('.')[-1])

            if colors:
                custom_style = CustomStyle
                custom_style.background_color = colors.get("background_color", "#272822")
                for token_type, color in colors.items():
                    setattr(custom_style, token_type, color)

                # Use TerminalTrueColorFormatter for higher color depth
                formatter = TerminalTrueColorFormatter(style=custom_style)
            else:
                # Use TerminalTrueColorFormatter for higher color depth
                formatter = TerminalTrueColorFormatter(style=CustomStyle)

            highlighted_code = highlight(code, lexer, formatter)

            if config.line_numbers:
                highlighted_code = '\n'.join(
                    f"{i+1:4}  {line}"
                    for i, line in enumerate(highlighted_code.splitlines())
                )

            print(highlighted_code)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    config_path = os.path.expanduser("~/.config/zat/config.json")
    config = Config(config_path)
    
    colors_config_path = os.path.expanduser("~/.config/zat/colors.json")
    colors = load_colors(colors_config_path)

    if len(sys.argv) < 2:
        print("Usage: python pretty_cat.py <filename>")
    else:
        filename = sys.argv[1]
        pretty_cat(filename, config, colors)
