


# Nueral Style Transfer
Pytorch implementation of Nueral style transfer algorithm , it is used to apply artistic styles to content images .  Content is the layout or the sketch and Style being the painting or the colors.

  

## Examples

  

![example 1](https://objectstorage.ap-hyderabad-1.oraclecloud.com/n/ax9kets4h5ld/b/github/o/example1.png)

![example 1](https://objectstorage.ap-hyderabad-1.oraclecloud.com/n/ax9kets4h5ld/b/github/o/example2.png)
# Getting Started

## Prerequisite

 - Python 3+ (tested on python 3.9)
 - pytorch
 - Nvidia Gpu(not necessary but it will significantly boost your training speed)
 
 

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/abhinav-TB/Neural-Style-Transfer.git
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
  
 
 ## Training
 

Command line Arguments

 | Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-s` | `string` | **Required**. path to style image |
| `-c` | `string` | **Required**. path to content image |
| `-e` | `string` | **Required**. Number of training loops |
| `-o` | `string` |  Output folder path |

start training
   ```sh
   python main.py
   ```
Example
   ```sh
   python main.py -s ./style/style5.jpg -c ./content/trees.jpg -e 2500 
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what makes the open source community such an amazing place to  learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<!-- LICENSE -->
##  License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

[@abhiGamez](https://twitter.com/abhiGamez) on Twitter

## Acknowledgements

 - [A Neural Algorithm of Artistic Styles](https://arxiv.org/abs/1508.06576)
 - [Neural Style Transfer: A Review](https://arxiv.org/abs/1705.04058)
