import streamlit as st
from model_helper import predict
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 3rem;
    }
    
    .upload-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .result-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        color: white;
        text-align: center;
    }
    
    .prediction-box {
        background: rgba(255,255,255,0.2);
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        text-align: center;
        margin: 1rem 0;
    }
    
    .stFileUploader > div > div > div > div {
        background: rgba(255,255,255,0.1);
        border: 2px dashed rgba(255,255,255,0.3);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<h1 class="main-header">🚗 Vehicle Damage Detection</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload an image to detect and analyze vehicle damage using AI</p>', unsafe_allow_html=True)

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Upload section
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("### 📤 Upload Vehicle Image")
    
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of the vehicle for damage detection"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Process uploaded file
if uploaded_file:
    # Create two columns for image and results
    img_col, result_col = st.columns([1, 1])
    
    with img_col:
        st.markdown("### 🖼️ Uploaded Image")
        # Display image with custom styling
        image = Image.open(uploaded_file)
        st.image(
            image, 
            caption="Vehicle Image for Analysis",
            use_container_width=True,
            output_format="JPEG"
        )
    
    with result_col:
        st.markdown("### 🔍 Analysis Results")
        
        # Add loading spinner
        with st.spinner('Analyzing image for damage...'):
            # Save temporary file
            image_path = "temp_file.jpg"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Get prediction
            try:
                prediction = predict(image_path)
                
                # Display result with custom styling
                st.markdown('<div class="result-section">', unsafe_allow_html=True)
                st.markdown("#### 🎯 Detection Result")
                st.markdown(f'<div class="prediction-box">🚨 {prediction}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Additional info based on prediction
                if "damage" in prediction.lower():
                    st.error("⚠️ Vehicle damage detected! Please consult a professional.")
                elif "no damage" in prediction.lower():
                    st.success("✅ No significant damage detected.")
                else:
                    st.info(f"📊 Classification: {prediction}")
                    
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
            
            finally:
                # Clean up temporary file
                if os.path.exists(image_path):
                    os.remove(image_path)

else:
    # Feature showcase when no file is uploaded
    # st.markdown("### ✨ Features")
    
    # col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     st.markdown("""
    #     <div class="feature-card">
    #         <h4>🤖 AI-Powered</h4>
    #         <p>Advanced machine learning model trained on thousands of vehicle images</p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col2:
    #     st.markdown("""
    #     <div class="feature-card">
    #         <h4>⚡ Fast Analysis</h4>
    #         <p>Get instant results with high accuracy damage detection</p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col3:
    #     st.markdown("""
    #     <div class="feature-card">
    #         <h4>📱 Easy to Use</h4>
    #         <p>Simply upload an image and get comprehensive damage analysis</p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # Instructions
    st.markdown("---")
    st.markdown("### 📋 How to Use")
    st.markdown("""
    1. **Upload Image**: Click the upload button above and select a vehicle image
    2. **Wait for Analysis**: Our AI model will process the image automatically  
    3. **View Results**: Get instant feedback about detected damage
    4. **Take Action**: Follow recommendations based on the analysis
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🔒 Your images are processed securely and not stored permanently</p>
    <p>Built with ❤️ using Streamlit and Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# import streamlit as st
# from model_helper import predict

# st.title("Vehicle Damage Detection")

# uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

# if uploaded_file:
#     image_path = "temp_file.jpg"
#     with open(image_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#         st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
#         prediction = predict(image_path)
#         st.info(f"Predicted Class: {prediction}")
