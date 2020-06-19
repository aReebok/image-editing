#include<iostream>
#include<fstream>

using namespace std;

struct Pixel {
   char red;
   char green;
   char blue;
};

class Image {
    int width, height;
    int depth;
    Pixel ** data;
public: 
    Image(const char * filename){
        ifstream f;
        f.open(filename);
        char* format = new char [3]; // stores P6 -- format
        f >> format >> width >> height >> depth;
        f.get();
        data  = new Pixel * [height];
        for (int i = 0; i < height; i++){ 
            data [i] = new Pixel [width]; 
        }
        for (int i = 0; i < height; i++) {
            f.read (reinterpret_cast<char*>(data[i]), 3*width) ;
        }
        f.close();
    }
    int getWidth() { return width; }
    int getHeight() { return height; }

    void print() {
        cout << "P6\n"<< width << " " << height << endl << depth << endl;
        for (int i = 0; i < height; i++) {
            cout.write(reinterpret_cast<char *>(data[i]), 3*width);
        }
    }
    void greyScale () {
        int average;
        for(int i = 0; i < height; i++){
            for (int j = 0; j < width; j++){
                average = (data[i][j].red + data[i][j].green + data[i][j].blue)/3;
                cout << "avg: " << average;
                data[i][j].red = data[i][j].green = data[i][j].blue = average;
            }
        }
    }


};

int main () {
    Image myimg("flower_0262.ppm");
    cout << "image height: " << myimg.getHeight() << endl;
    cout << "image width: " << myimg.getWidth() << endl;
    myimg.greyScale();

}

