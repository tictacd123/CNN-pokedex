
import streamlit as st
from PIL import Image
import numpy as np
import time
from keras.models import load_model
import cv2
import tensorflow

model = load_model("model_pokedex.h5")

def predict(img_to_predict):
    print(model.predict_classes(img_to_predict))
    print(model.predict(img_to_predict))
    res=model.predict(img_to_predict)[0][1]
         
    return res

st.title("CNN Pokemon Detector App")
st.write('\n')

image = Image.open('pokedex.jpg')
show = st.image(image, use_column_width=True)

st.sidebar.title("Choisissez une image de Pikachu ou de Rondoudou")

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    
    u_img = Image.open(uploaded_file)
    show.image(u_img, 'Image', use_column_width=True)
    img_array = np.array(u_img)

    img_to_predict = np.expand_dims(cv2.resize(img_array,(200,200)), axis=0) 


st.sidebar.write('\n')
    
if st.sidebar.button("Détecter le pokemon"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Ajoutez une image pour commencer la détection")
    
    else:
        
        with st.spinner('Identification'):
            
            prediction = predict( img_to_predict)
            time.sleep(2)
            st.success('Pokemon identifié !')
            
        st.sidebar.header("Résultat")
        
        if prediction <  0.5:
            
            st.sidebar.write("C'est un pikachu!", '\n' )
            
            st.sidebar.write('**Probabilité: **',"{:.3f}".format(float(100-prediction*100)),'%')
     
            
            
                             
        else:
            st.sidebar.write(" C'est un Rondoudou ",'\n')
            
            st.sidebar.write('**Probabilité: **',"{:.3f}".format(float(prediction*100)),'%')
   


st.sidebar.write('\n')
st.sidebar.write('\n')
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')
st.sidebar.write('\n')
st.sidebar.write('\n')
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')  
st.sidebar.write('\n')                
            
st.sidebar.write("Par [tictacd123](https://github.com/tictacd123) pour le cours de ML")
    
    
    