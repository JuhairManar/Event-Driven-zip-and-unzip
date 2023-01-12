import glob
import shutil
import os
import zipfile
import runpy

source_path='..\source\*'
destination_path='..\destination'

source_object=glob.glob(source_path)
 
object_path=source_object[0]
print("\n")

shutil.copy(object_path,'.') 
this_directory=os.getcwd()
print(this_directory)
object_name=object_path.split('\\')[-1].split('.')

prefix=object_name[0] #some
postfix_2=object_name[1]



temp=0
if postfix_2=='txt':
    with zipfile.ZipFile('..\destination\All_files.zip','w') as f:
        for i in range(3):
            filename=prefix+'_'+str(i+1)+'.'+postfix_2   
            #shutil.copy(object_path,filename) 
            with open (source_object[0],'r') as rf,open(filename,'w') as wf:
                j=0
                for line in rf:
                    if j==(i+1)*10:
                        j=0
                        break
                    wf.write(line)
                    j+=1

            f.write(filename)
            print("\n")
            l=f'{this_directory}\{filename}'
            os.remove(l.split('\\')[-1])
        f.extractall(destination_path)   

elif postfix_2=='py':
    try:
        runpy.run_module(mod_name=object_name[0])
    except:
        print("An exception occurred") 

else:
    print("We have no operation for this file type")           



os.remove(object_path)   
os.remove(object_path.split('\\')[-1])  

#runpy,exec method

"""
    print('\n')
    print('\n')
    print(filename)
    shutil.move(filename,destination_path)
    fn=f'{destination_path}\{filename}'
    print(destination_path)
    #shutil.unpack_archive(f'{destination_path}\\{fn}',destination_path)
    shutil.unpack_archive(f'./{filename}','.')
"""

""" Successfull

with zipfile.ZipFile('..\destination\All_files.zip','w') as f:
    for i in range(3):
        filename=prefix+'_'+str(i+1)+'.'+postfix_2   
        shutil.copy(object_path,filename) 
        f.write(filename)
        print("\n")
        l=f'{this_directory}\{filename}'
        os.remove(l.split('\\')[-1])
    f.extractall(destination_path)   """


#to undo just comment out line 31-38    