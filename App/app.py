import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


st.set_option('deprecation.showfileUploaderEncoding', False)

def prediction(image, model):

	image = tf.cast(image, tf.float32)
	image = tf.image.resize(image, [256, 256])

	image = np.expand_dims(image, axis = 0)

	return model.predict(image)

	


model = tf.keras.models.load_model('model.h5')
st.title('Brain tumor prediction using MR Images...')
st.write('TEAM Zyndicate')


def main():
	file = st.file_uploader("Upload an MR Image......", type=["jpg", "png"])


	if file is None:
		st.text('Waiting for upload....')
     
	else:
		slot = st.empty()
		slot.text('Predicting........')

		test_image = Image.open(file)

		st.image(test_image, caption="Input Image", width = 400)
 
		pred = prediction(np.asarray(test_image), model)

		df_class_names = ['category1_tumor', 'category2_tumor', 'category3_tumor', 'no_tumor']

		result = df_class_names[np.argmax(pred)]
 
 
		if(result == 'category1_tumor'):
			status = 'Category 01 tumor'
		elif(result == 'category2_tumor'):
			status = 'Category 02 tumor'
		elif(result == 'category3_tumor'):
			status = 'Category 03 tumor'
		else :
			status = 'No tumor'

		slot.text('Done')
		st.success('Detect as a ' + status)
  
  
if __name__ == '__main__':
    main()

	
 

