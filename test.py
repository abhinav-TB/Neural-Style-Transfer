import argparse
 
 
parser = argparse.ArgumentParser()
 


parser.add_argument("-s", "--style", help = "Style Image path" , required=True)
parser.add_argument("-c", "--content", help = "Content Image path" , required=True)
parser.add_argument("-e", "--epochs", help = "Number of Epocs" , required=True)

 
args = parser.parse_args()
 
print(args.epochs)