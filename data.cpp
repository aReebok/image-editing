// creates a file that holds the mean of RGB
// composition for each 30x30 small images

#include <iostream>
#include <fstream>
using namespace std;


using namespace std;

struct Pixel {
   char red;
   char green;
   char blue;
};

class Image{
    int width, height;
    int depth;
    Pixel ** data;
public:
    Image(int w, int h){
        width = w;
        height = h;
        depth = 255;
        data = new Pixel * [height];
        for (int i =0; i < height; i++){ 
            data [i] = new Pixel [width]; 
        }
    }
    Image(const char * filename){
        ifstream f;
        f.open(filename);
        char* format = new char [3];
        format [2] = 0;
        f  >> format >> width >> height >> depth;
        f.get();
        //delete [] data;
        data = new Pixel * [height];
        for (int i = 0; i < height; i++){ 
            data [i] = new Pixel [width]; 
        }
        for (int i = 0; i < height; i++) {
            f.read (reinterpret_cast<char*>(data[i]), 3*width) ;
        }
        f.close();
        cerr << width << endl << height << endl;
    }

    ~Image(){ 
        for (int i = 0; i < height; i++) { delete [] data [i]; }
        delete [] data; 
    }
    int getWidth() { return width; }
    int getHeight() { return height; }
    Pixel ** getData() { return data; }

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

    void horizSqueeze () {
        Image temp = *this;
        delete [] data;

        data = new Pixel * [height];
        for (int i = 0; i < height; i++){ 
            data [i] = new Pixel [width/2]; 
        }
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width/2; j++){ ///012345 02468...
                data [i][j].red = temp.data[i][2*j].red;
                data [i][j].green = temp.data[i][2*j].green;
                data [i][j].blue = temp.data[i][2*j].blue;

            }
        }
        width = width/2;
    }

    void print() {
        cout << "P6\n"<< width << " " << height << endl << depth << endl;
        for (int i = 0; i < height; i++) {
            cout.write(reinterpret_cast<char *>(data[i]), 3*width);
        }
    }
};

int main () {
    Image myimg("flower_0262.ppm"); 
    //myimg.greyScale();
}
