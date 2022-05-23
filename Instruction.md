# Instruction

## L_System.exe

* Num iteration -- Number of transformin the String (0 -- start String).
* Start -- First String we start with;
* Rule (1-5) -- Different rules that transform current String;
	* First column -- one character that will transform into subString;
	* Second column -- the subString to which char will transform;
* Step -- Lenght of line drawing;
* Turn -- Angle of rotation;
* Fill -- Filling or not;
* Position -- Start position;
* Rotation -- Start rotation;
* Resize -- Level of compression result image (1 -- original size, >1 -- compresion);
* Start -- Starting of image generation;
* Path -- Select the path for saving;
* Save -- Save the png image;
* Save settings -- Save information about current setting into txt file.

#### Type of character:
* Upper letter (A-Z) -- one step forward with drawing;
* lower letter (a-z) -- one step forwar without drawing;
* '+' and '-' -- turn right and left in degrees;
* '[' and ']' -- save and load position and turning degree;
* '^' and '_' -- pen up and down.

## Tree.exe

* Rand step -- Variation of length in the range of +- given number;
* Rand turn -- Variation of angle in the range of +- given number.

#### Type of character:
* '0' -- leaf, that will grow;
* '1' -- stalk (has a chance to create a new leaf);
* '2' -- stalk;
* '+' and '-' -- turn right and left in degrees;
* '[' and ']' -- save and load position and turning degree;
* '^' -- random turning (left or right).



## TreeAnim.exe

* Sleep time -- Waiting time between every frame;
* Saving -- Taving all frame into png file.



## Some problems

* When you save canvas you got ps file. You can convert this file manually;
* Otherwise you can download Ghostscript (32 bit) to convert it automatically.
