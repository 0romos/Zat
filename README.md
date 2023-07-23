
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/0romos/Zat">
    <img src="https://media.discordapp.net/attachments/1128669686234615950/1132759673423024168/zatIcon.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Zat</h3>

  <p align="center">
    Elevate Your File Reading Experience
    <br />
    <a href="https://github.com/0romos/Zat"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/0romos/Zat/">View Demo</a>
    ·
    <a href="https://github.com/0romos/Zat/issues">Report Bug</a>
    ·
    <a href="https://github.com/0romos/Zat/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
    </li>
    <li>
      <a href="#installation">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<br />
<center> <h1 align="left" id="about">About</h1> </center>

Zat is a sleek and modern file reader for Linux, purrfectly designed to elevate your file reading experience. Embrace the power of the feline charm as you effortlessly navigate and unite files with finesse. Enjoy a seamless and delightful command-line journey with Zat!

![image](https://media.discordapp.net/attachments/1115614887658410085/1132759924674404523/image.png)

<br />
<center> <h1 align="left" id="installation">Installation</h1> </center>

_Below is an example of how you can instruct your audience on installing and setting up your binary file. This template doesn't rely on any external services._

1. Clone the repo
   
   ```sh
   git clone https://github.com/0romos/Zat.git
    ```

   ```sh
   python3 -m pip install cutepy
    ```

<br />
<center> <h1 align="left" id="usage">Usage</h1> </center>

1. Run Zat
    ```
    python3 src/zat.py <file / path to file>
    ``` 

2. Create an Alias (`Add this at the end of .bashrc / .zshrc and so on`)
    ```
    alias zat="python3 path/to/zat.py"
    ```

3. Reopen a terminal and run zat
    ```
    zat <file / path to file>
    ```
    
See the [open issues](https://github.com/0romos/Zat) for a full list of proposed features (and known issues).

<br />
<center> <h1 align="left" id="configuration">Configuration</h1> </center>

Upon execution, the application will conduct a thorough examination to verify the presence of a designated 'zat' folder, as well as the existence of the `config.json` and `colors.json` files within said `zat` directory, situated in the user's designated configuration path at `$HOME/.config/zat`. In the event that these essential components are not discovered, the application will initiate their creation, ensuring a seamless user experience. Notably, the color schemes are effortlessly modifiable, affording users the opportunity to craft and integrate personalized schemes effortlessly.

1. config.json

    ```json
    {
        "highlight": true,
        "line_numbers": true
    }
    ```

2. colors.json

    ```json
    {
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
    
    ```

<br />
<center> <h1 align="left" id="contributing">Contributing</h1> </center>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b new-dev-20220608`)
3. Commit your Changes (`git commit -m 'Added Language Support'`)
4. Push to the Branch (`git push origin new-dev-20220608`)
5. Open a Pull Request


<!-- LICENSE -->
<br />
<center> <h1 align="left" id="license">License</h1> </center>

Distributed under the MIT License. See `LICENSE` for more information.
    
