from PIL import Image
words=Image.open('c:\\Users\\Admin\\Desktop\\Complete-Python-3-Bootcamp-master\\14-Working-with-Images\\word_matrix.png')
masker=Image.open('c:\\Users\\Admin\\Desktop\\Complete-Python-3-Bootcamp-master\\14-Working-with-Images\\mask.png')
masker = masker.resize((1015,559))
data = masker.getdata()
newdata=[]
for item in data:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newdata.append((255,255,255,0))
    else:
        newdata.append(item)
masker.putdata(newdata)
words.paste(im=masker,box=(0,0),mask=masker)
words.show()