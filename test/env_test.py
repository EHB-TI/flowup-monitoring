import sys ,os, pytest
  
def test_env_readable():
    x=0
    try:
        with open('.env') as f:        
            x=1        
    except IOError:
        print("File not accessible")    
    assert x ==1

def test_env_isExists():
    # When the env file is correctly "configured" the size of the file should be equal to 1136
    x= os.stat('.env').st_size
    assert x == 1136