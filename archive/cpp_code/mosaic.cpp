// #include <stdio.h>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

#define FLOWERFILE "flower_info"

using namespace cv;
using namespace std;
namespace fs = std::filesystem;

void mosaic(string file_name, string output_name, int precision);
void parse_flowers();
void read_flowers();
// void cpp_mosaic(string, string, int);

Mat get_flower(int, int, int);

struct Flower {
    string file;
    int red, blue, green;
};

vector<Flower> flowers; 

int main(int argc, char** argv ) {
    if ( argc  < 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    string filename = argv[1];
    string output = argv[2];

    parse_flowers();
    read_flowers();
    mosaic(filename, output, 1);
}

void parse_flowers() {
    string path = "./../flowers/";
    Mat image;
    uchar * p;
    int red, green, blue;

    ofstream myfile(FLOWERFILE);

    for (const auto & entry : fs::directory_iterator(path)) {
        red = 0; green = 0; blue = 0;
        image = imread(entry.path());
        int channels = image.channels();
        int nRows = image.rows;
        int nCols = image.cols * channels;

        for (int i = 0; i < nRows; i++) {
            p = image.ptr<uchar>(i);
            for (int j = 0; j < nCols; j+=3) {
                blue += p[j];
                green += p[j+1];
                red += p[j+2];
            }
        }

        blue =  blue / (image.rows * image.cols);
        green =  green / (image.rows * image.cols);
        red =  red / (image.rows * image.cols);
        myfile<< entry.path() << " " << red << " " << green << " " << blue << endl;        
    }
    myfile.close();
}

void read_flowers() {
    ifstream ifs(FLOWERFILE);
    string name;
    int red, blue, green;
    while (ifs >> name) {
        ifs >> red >> green >> blue;
        name.pop_back();
        name.erase(0, 1);
        Flower f;
        f.file = name;
        f.red = red;
        f.blue = blue;
        f.green = green;
        flowers.push_back(f);
    }
}

void mosaic(string file_name, string output_name, int precision) {

    Mat image, flow;
    image = imread( file_name, 1 );
    if ( !image.data ) {
        printf("No image data \n");
        return;
    }

    int channels = image.channels();
    int nRows = image.rows;
    int nCols = image.cols * channels;

    uchar * imgPtr, *floPtr;
    int r=0,g=0,b=0;
    string flower = "";
    int size = 20;

    for (int i = 0; i < nRows; i += size) {
        for (int j = 0; j < nCols; j += size * 3) {
            for (int k = 0; k < size; k++) {
                imgPtr = image.ptr<uchar>(i + k);
                for (int l = 0; l < size * 3; l+=3) {
                    b += imgPtr[j+l];
                    g += imgPtr[j+l+1];
                    r += imgPtr[j+l+2];
                }
            }
            b /= size * size;
            g /= size * size;
            r /= size * size;
            flow = get_flower(r,b,g);
            for (int k = 0; k < size; k++) {
                if (i + k >= nRows) {break;} 
                imgPtr = image.ptr<uchar>(i+k);
                floPtr = flow.ptr<uchar>(k);
                for (int l = 0; l < size*3; l +=3) {
                    if (j+l >= nCols) {break;} 
                    imgPtr[j+l] = floPtr[l];
                    imgPtr[j+l+1] = floPtr[l+1];
                    imgPtr[j+l+2] = floPtr[l+2];
                } 
            }
        }
    }
    imwrite(output_name, image);
}

Mat get_flower(int red, int blue, int green) {
    Mat image;
    int value, best = INT32_MAX, index = 0;

    for (int i = 0; i < flowers.size(); i++) {
        value = pow(red- (flowers[i].red), 2) + pow(green - (flowers[i].green), 2) + pow(blue - (flowers[i].blue), 2);
        if (value < best) {
            best = value;
            index = i;
        }
    }
    image = imread(flowers[index].file, 1);
    return image;
}