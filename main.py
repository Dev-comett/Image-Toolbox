import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

st.set_page_config(
    page_title="ToolsHub | ImageToolbox",
    layout="wide",
    page_icon="🛠️"
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #4a90e2;
            text-align: center;
            margin-bottom: 1em;
        }
        .stButton>button {
            background-color: #4a90e2;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6em 1.2em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #3a78c2;
            transform: scale(1.05);
        }
        footer {
            text-align: center;
            padding: 1em 0;
            margin-top: 3em;
            color: #888;
        }
        .social-icons img {
            width: 24px;
            height: 24px;
            margin: 0 10px;
            vertical-align: middle;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">ToolsHub: ImageToolbox</div>', unsafe_allow_html=True)

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", width=500)

    option = st.selectbox(
        "Choose a tool",
        ["Crop", "Resize", "Rotate", "Convert to Grayscale", "Flip Horizontal", "Flip Vertical",
         "Blur", "Adjust Brightness", "Adjust Contrast", "Convert Format"]
    )

    processed_img = image

    if option == "Crop":
        st.subheader("Crop Image")
        st.info("Drag to select crop region")
        from streamlit_cropper import st_cropper
        cropped_img = st_cropper(image, box_color='#4a90e2', aspect_ratio=None)
        if st.button("Apply Crop"):
            processed_img = cropped_img
            st.image(processed_img, caption="Cropped Image", width=500)

    elif option == "Resize":
        st.subheader("Resize Image")
        new_width = st.number_input("New Width", 1, 2000, image.width)
        new_height = st.number_input("New Height", 1, 2000, image.height)
        if st.button("Apply Resize"):
            processed_img = image.resize((new_width, new_height))
            st.image(processed_img, caption="Resized Image", width=500)

    elif option == "Rotate":
        st.subheader("Rotate Image")
        angle = st.slider("Rotation Angle", 0, 360, 0)
        if st.button("Apply Rotation"):
            processed_img = image.rotate(angle)
            st.image(processed_img, caption="Rotated Image", width=500)

    elif option == "Convert to Grayscale":
        st.subheader("Convert to Grayscale")
        if st.button("Apply Grayscale"):
            processed_img = image.convert("L")
            st.image(processed_img, caption="Grayscale Image", width=500)

    elif option == "Flip Horizontal":
        st.subheader("Flip Image Horizontally")
        if st.button("Apply Horizontal Flip"):
            processed_img = image.transpose(Image.FLIP_LEFT_RIGHT)
            st.image(processed_img, caption="Flipped Horizontally", width=500)

    elif option == "Flip Vertical":
        st.subheader("Flip Image Vertically")
        if st.button("Apply Vertical Flip"):
            processed_img = image.transpose(Image.FLIP_TOP_BOTTOM)
            st.image(processed_img, caption="Flipped Vertically", width=500)

    elif option == "Blur":
        st.subheader("Blur Image")
        radius = st.slider("Blur Radius", 0.0, 10.0, 2.0)
        if st.button("Apply Blur"):
            processed_img = image.filter(ImageFilter.GaussianBlur(radius))
            st.image(processed_img, caption="Blurred Image", width=500)

    elif option == "Adjust Brightness":
        st.subheader("Adjust Brightness")
        factor = st.slider("Brightness Factor", 0.1, 3.0, 1.0)
        if st.button("Apply Brightness"):
            enhancer = ImageEnhance.Brightness(image)
            processed_img = enhancer.enhance(factor)
            st.image(processed_img, caption="Brightness Adjusted", width=500)

    elif option == "Adjust Contrast":
        st.subheader("Adjust Contrast")
        factor = st.slider("Contrast Factor", 0.1, 3.0, 1.0)
        if st.button("Apply Contrast"):
            enhancer = ImageEnhance.Contrast(image)
            processed_img = enhancer.enhance(factor)
            st.image(processed_img, caption="Contrast Adjusted", width=500)

    elif option == "Convert Format":
        st.subheader("Convert Image Format")
        format_option = st.selectbox("Select Format", ["JPEG", "PNG"])
        if st.button("Convert Format"):
            img_bytes = io.BytesIO()
            processed_img.save(img_bytes, format=format_option)
            img_bytes.seek(0)
            st.download_button(
                label=f"Download as {format_option}",
                data=img_bytes,
                file_name=f"converted_image.{format_option.lower()}",
                mime=f"image/{format_option.lower()}"
            )
            st.image(processed_img, caption=f"Converted to {format_option}", width=500)

    if option != "Convert Format" and processed_img != image:
        img_bytes = io.BytesIO()
        processed_img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        st.download_button(
            label="Download Processed Image",
            data=img_bytes,
            file_name="processed_image.png",
            mime="image/png"
        )

    st.markdown("---")
    st.info("Tip: After applying any tool, you can download your result using the button below.")

else:
    st.warning("Please upload an image to start editing.")

# Footer
st.markdown("""
    <footer>
        Made with ❤️ by <strong>Im_Dev</strong><br>
        <div class="social-icons">
            <a href="https://github.com/dev-comett" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
            </a>
            <a href="https://linkedin.com/in/dev-ice" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
            </a>
        </div>
    </footer>
""", unsafe_allow_html=True)
