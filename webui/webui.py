import gradio as gr
from wording import get
import batch_option
import text_options
import seed_option
import aduio_option
import enhance_option
import output_option
import config_option
from webuiutils import read_config, get_server_config



def main():
    try:
        with gr.Blocks(theme=gr.themes.Soft()) as demo:
            gr.Markdown(get('Title'))
            gr.Markdown(get('VersionDescription'))
            with gr.Row():
                with gr.Column():
                    batch_option.render()
                    with gr.Row():
                        gr.Markdown(get('TextOptionsTitle'))
                    text_options.render()
                    with gr.Row():
                        gr.Markdown(get('SeedOptionsTitle'))
                    seed_option.render()
                    with gr.Row():
                        gr.Markdown(get('AudioOptionsTitle'))
                    aduio_option.render()
                    with gr.Row():
                        gr.Markdown(get('AudioEnhancementTitle'))
                    enhance_option.render()

                with gr.Column():
                    output_option.render()
                    gr.Markdown(get('configmanager'))
                    config_option.render()
                    with gr.Accordion(get('HelpTitle'), open=False):
                        gr.Markdown(get('HelpContent'))
                        with gr.Row():
                            gr.Markdown(" ")
                        with gr.Row():
                            gr.Markdown(" ")
                    with gr.Row():
                        gr.Markdown('🔧项目地址:https://github.com/CCmahua/ChatTTS-Enhanced')

            batch_option.listen()
            text_options.listen()
            seed_option.listen()
            aduio_option.listen()
            enhance_option.listen()
            output_option.listen()

        config = read_config('config.ini')
        custom_server, ip_address, port = get_server_config(config)
        
        # 修改启动参数
        kwargs = {
            "inbrowser": False,  # 改为False，不自动打开浏览器
            "server_name": "0.0.0.0",  # 允许远程访问
            "server_port": port if custom_server else 7860,
            "share": False  # 不使用gradio的分享功能
        }
        
        print(f"\n界面启动成功！请在浏览器中访问: http://{ip_address}:{kwargs['server_port']}\n")
        demo.launch(**kwargs)
        
    except Exception as e:
        print(f"Error starting webui: {str(e)}")
        raise



if __name__ == '__main__':
    main()