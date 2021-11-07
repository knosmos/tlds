# Too Long Didn't Solve

## Inspiration
Our school has a 3D printer with a broken extruder. Since **global electronic waste** is a big issue in our society (53.6 million metric tons of e-waste were produced in 2019), we wanted to set an example to encourage others to give a new purpose to old electronics. We also hoped to inspire the next generation of computer scientists by making them excited about programming.

## What it does
TL;DS is an **automatic math homework solver**. It can take a photo of a math problem, solve the math problem and hand-write the answer using the 3D printer. TL;DS also has an experimental feature that allows it to draw graphs on paper.

## How we built it
TL;DS is built with a variety of different tools. The web application, where images can be captured and uploaded, is built with Flask. After the image is uploaded, TL;DS uses **optical character recognition** from Tesseract to read text off the image, and a custom library along with a tool called GPX to write the instruction file for the 3D printer. 

## Challenges we ran into
There were several major issues we encountered while building TL;DS. The OCR sometimes did not detect the text properly; we remedied this by **preprocessing images** with OpenCV. As this project involves hardware, we encountered some physical problems; for example, the pen was often unstable and either had too much or too little pressure. To fix this, we used a pen spring to provide the **correct amount of pressure**. Additionally, the Makerbot printer uses a binary file format called X3G, which requires the usage of a gcode-to-x3g converter.

## Accomplishments that we're proud of
- Building a functional and consistent handwriting machine in a limited time span
- Mostly reliable OCR and mathematical equation solving
- Easy-to-use web application to facilitate image capture and transfer to computer for processing

## What we learned
While we already had experience using 3D printers, writing low-level instructions to control them (as opposed to dragging a model into Slic3r) gave us a lot of insight on how 3D printers work. We also learned how important it is to continuously iterate on a design; both our OCR and especially the pen holder went through many iterations to try to achieve an optimal result.

## What's next for TL;DS
- Ability to solve and write **multiple equations** from a single image (currently only supports one equation at a time)
- Integration of Wolfram|Alpha, and usage of MathPix OCR instead of Tesseract, to enable recognition and solving of more complex mathematical problems
- End-to-end automated workflow - currently, after the photo is sent to the computer, the application writes the file onto an SD card that must be manually transferred to the printer. In the future, the file could be directly transferred using a cable.
- 3D-printed pen cartridge housing, for even better stability and control of handwriting
