# Python-Scripting-for-ArcGIS using NumPy
• This Python script creates a geodatabase and names it.

• loops through all raster datasets and feature classes in the geodatabase to check if they are projected or not.

• If they are not projected, it projects them within the new geodatabase that was created in the first step.

• Changes the current workspace to the new geodatabase.

• It uses Numpy to calculates the ratio of total forest land cover [ codes: 41, 42, 43] to total developed land cover [ codes: 21, 22, 23, 24] for each zipcode area.

• This is a Zonal Operation problem.

• It creates a text file and reports the zip code and the ratio of forest to urban in the text file.
