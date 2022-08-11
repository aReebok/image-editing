# Python Image and Video Mosaic API by Areeba and Kaashya

## Usage

### Create a mosaic image

**Definition**

`POST /image`


```json
{
    "userID": "User ID of the user who made the request",
    "imageURL": "Holds the image URL to be downloaded and converted",
}
```

This command takes an image attachment in the form of a URL (or discord attachment url) and also takes userID. 

**Response**

Sends back a string of what the image was stored as in the database for it to be called again by using get. 

### Get the status of an image by its name

`GET /image/status/<path>`

Gets the current status of a specified image

**Response**

This command will respond with the current status of the input image:
- NotFound: means that the image was not found.
- Encripting: means that the image is going through the mosaic algorithm.
- Complete: means that the image process is complete and is ready to be shared using get. 

### Get a created image by its name

`GET /image/<path>`

Returns url of given image name.

**Response**

URL of image.

