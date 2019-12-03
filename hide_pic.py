from stegano import lsb

import argparse
import os
import sys
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="Encrypt a message in an image", action='store_true')
    parser.add_argument("-d", help="Decrypt a message in an image", action='store_true')
    parser.add_argument("image_dir", help="The image dir that you want to encrypt/decrypt")
    args = parser.parse_args()

    if "~" in args.image_dir:
        format_image_dir = args.image_dir.replace("~", os.environ['HOME'])
    else:
        format_image_dir = args.image_dir

    if not os.path.exists(format_image_dir):
        print("The image path given does not exist")
        sys.exit()
    


    if args.e:
        message = input("What message would you like to encrypt the photo with? ")
        secret = lsb.hide(format_image_dir, message)
        base_name = os.path.basename(format_image_dir)
        hidden_file = base_name[:-4] + "-secret" + base_name[-4:]
        secret.save(hidden_file)
        print("Success, we have created a photo with the message hidden called {}".format(hidden_file))
    if args.d:
        secret_message = lsb.reveal(format_image_dir)
        if secret_message:
            print("Your secret message is: " + secret_message)
        else:
            print("There is either no message hidden, or we can't detect the message!")

if __name__ == "__main__":
    main()