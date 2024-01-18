#!/usr/bin/env python

import argparse
import obj_predictor.data_processing.gen_image_variations as gen_img_vars

'''
Created by Jacob Rivera
Fall 2024

Last edit: 01/17/2024

Description:
    Mirror image and annotation file across y axis

'''
### NOT TESTED YET ###





def main():
    parser = argparse.ArgumentParser(description="Mirror an image and annotation file across x and y axis")
    parser.add_argument("--input_img", required=True, help="input image")
    parser.add_argument("--input_txt", required=True, help="input text file")
    parser.add_argument("--output_img", required=False, help="output image")
    parser.add_argument("--output_txt", required=False, help="output text file")

    args = parser.parse_args()

    input_img = args.input_img
    input_txt = args.input_txt
    output_img = args.output_img
    output_txt = args.output_txt


    if output_img is None:
        output_img = input_img.replace(".jpg", "_mirror_acr_xy.jpg")
    if output_txt is None:
        output_txt = input_txt.replace(".txt", "_mirror_acr_xy.txt")

    gen_img_vars.flip_image_vertically(input_img, output_img)

    width, height = gen_img_vars.get_image_resolution(input_img)

    gen_img_vars.process_text_file(input_txt, output_txt, width, height, 'xy')

    return

if __name__ == "__main__":
    main()