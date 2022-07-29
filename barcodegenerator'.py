#inorder to use this program you have to first install the barcode pacakge in python.
from barcode import EAN13
from barcode.writer import ImageWriter 
num_of_barcodes=int(input("Enter the number of Barcodes you want to generate"))
numbers=range(num_of_barcodes)
for i in numbers:
    id=input(" Give 12-Digit numbers for your barcode id: ")
    my_code=EAN13(id,writer=ImageWriter)
    name = input("Give name for the barcode: ")
    my_code.save(name)
