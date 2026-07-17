import gradio as gr

def process_data(input_img, input_text):
    output_img = input_img

    output_text = f"Kết quả xử lý từ '{input_text}': Đã hoàn thành!"
    return output_img, output_text


image_in = gr.Image(label="Ảnh đầu vào")
text_in = gr.Textbox(label="Văn bản đầu vào")

image_out = gr.Image(label="Ảnh kết quả")
text_out = gr.Textbox(label="Văn bản kết quả")

demo = gr.Interface(
    fn=process_data,
    inputs=[image_in, text_in],
    outputs=[image_out, text_out]
)

demo.launch()
