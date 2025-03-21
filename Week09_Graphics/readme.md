# Class 9 - March 21st 2025
- In this class we will:
    - Discuss concepts related to graphics
    - Learn tips and tools for making better figures
    - Work with a few different programs for building/modifying figures

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 17-19


### Vector Assignments

1. Work through tutorials specific for your program. 

    a. If you are using Inkscape, read through both the [Basic](https://inkscape.org/en/doc/tutorials/basic/tutorial-basic.html) and [Advanced](https://inkscape.org/en/doc/tutorials/advanced/tutorial-advanced.html) tutorials. These links are to the static html versions on the Inkscape website, but these can also be accessed within the Inkscape program with Help > Tutorials. This will bring you to an interactive version. Make sure to try all of the explained commands within the Inkscape program. 

    b. If you are using Illustrator, work through this [vector basics tutorial](https://www.youtube.com/watch?v=GFY0_EMVYDw&feature=youtu.be).


1. HapNetwork.pdf (or HapNetwork.svg) contains a vector-based haplotype network depicting the relationships among several Ebola virus genomes from the West African outbreak. The PDF version should work well for Illustrator, SVG will be better for Inkscape.

    1. First, remove the background grey shapes. 

    2. Second, use the "Select -> Same" tool to quickly adjust the color scheme to something recommended on [ColorBrewer2](http://colorbrewer2.org). 

    3. Finally, change the location names to the names (or Hex Codes) of your chosen colors.

    4. **Save your edited version of the haplotype network and upload to Canvas.**

2. Open scatter.pdf (or scatter.svg) in your vector editor of choice. This file contains a scatterplot generated using the Python module Matplotlib. Before getting started with the following tasks, use the "Direct selection" or "Edit paths by nodes" tool to select and explore various objects in the graph. There are probably a lot more objects than you would have predicted. This is often the case with figures exported from programs such as Python, R, and Matlab. 

    1. This figure will be used in a manuscript, with a width of only 1/3 of a page. Increase the size of of the axis tick labels for clarity in the printed version...notice somethng unexpected? Even within a vector-based graphic, numbers and letters are not always output as editable text. In this case, you have two options: 1) keep the numbers simply as shapes and enlarge them using a combination of the two arrow tools or 2) delete the existing labels and use the Type tool to replace them with editable text versions. These can then be resized just as you would resize text in Word. 

    2. Next, use the Type tool to add x- and y-axis labels. The y-axis label should be "log(unique 19mers in cluster)" and the x-axis label should be "log(# of sequences)". Make sure the labels will be easily visible in printed form. 

    3. To allow for easier editing, use the 'Select -> Same' tool to move similar elements (e.g., elements with the same fill and stroke) onto different layers. Go ahead and hide the layers containing elements with red/blue stroke, but transparent fill. If you are using the .pdf formatted file, also hide the layer containing elements with transparent stroke AND fill. 

    4. Note how your impression of the data changes depending on whether the layer with the blue circles is above or below the layer with the red circles. To better visualize the overlapping points, convert the fill of all the circles to 50% transparency. 
    
    5. **Save your edited version of the scatter image and upload to Canvas.**

3. **Extra Credit** tarantula.jpg is a photo of a tarantula that my dad found on a golf course in Tulsa, OK. 
    1. Use the Pen tool to trace the tarantula using bezier curves. This will allow you to generate a simplified vector version that could be used in a presentation or a figure. Make sure that your trace is placed in a separate layer from the starting image. 

    2. As an alternative approach to the same goal, play around with the [Image Trace function](https://helpx.adobe.com/illustrator/using/image-trace.html) if you're using Illustrator or [Trace Bitmap](https://inkscape-manuals.readthedocs.io/en/latest/tracing-an-image.html) if you're using Inkscape.
    
    3.  **Save your vector-based version of the tarantula and upload to Canvas.**


### Pixel Assignments

1. Open Gel.jpg in either Photoshop or GIMP. This file contains an underexposed image of an agarose gel. Play with the levels (as described in PCfB p. 376-386) to see how this changes the appearance of the image. Save the new levels as a distinct layer (Photoshop: Layer > New Adjustment Layer > Levels..., GIMP: Layer > Duplicate Layer, then Colors > Levels...) to make it easy to toggle between the new and original levels.

2. On your version of Gel.jpg (with the new levels; please make sure these are easily differentiated from the original levels), use the Type/Text tool to add annotations to the image. The bands on the left are from a molecular weight size marker (i.e. a ladder) and the bands on the right are viral genome segments. Feel free to choose whatever labels you want. 

3. **Save your edited version of Gel.jpg and upload to Canvas.**

4. **Extra Credit** Another possibility for generating an image of the tarantula for a presentation (as opposed to creating a vector-based version) would be to create a simplified pixel-based version by removing all of the background. In Illustrator, play around with the various lasso tools to select and delete the background material. Or try [these approaches](https://www.howtogeek.com/731327/how-to-remove-a-background-in-photoshop/).  Here are some [good tools for GIMP](https://docs.gimp.org/en/gimp-tutorial-quickie-separate.html). Here is another [cool approach](https://www.youtube.com/watch?v=XXReaZw013k). **Upload your background-removed version of the tarantula to Canvas.**


### BioRender Extra Credit

1. Sign up for a free [BioRender](https://www.biorender.com/) account.

2. Use BioRender to generate a figure to accompany your project proposal and include this figure in your project proposal submission. 


## Extra fun

[Complete Beginner's Guide to Adobe Illustrator](https://pdfcoffee.com/illustrator-for-beginners-tastytuts-pdf-free.html)

[BioRender Tutorials](https://www.biorender.com/learn)



Copyright (C) 2025  Jason Ladner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.



