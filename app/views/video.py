import streamlit as st
from services.transcript import get_transcript


def Video():
    st.write("Video IA")
    st.write("Upload a video to get the transcript")
    file = st.file_uploader("Upload a video", type=['mp4', 'avi', 'mov'])
    
    if file:
        st.write("File uploaded")
        st.video(file)
        if st.button("Get transcript"):
            with open('video.mp4', 'wb') as f:
                f.write(file.getvalue())

            transcript = get_transcript('video.mp4')
            print_transcript(transcript)
        
    else:
        st.write("No file uploaded")
    
def print_transcript(transcript):
    st.write('language: ', transcript['language'])

    if len(transcript['segments']) > 0:
        for segment in transcript['segments']:
            start = int(segment['start'])
            end = int(segment['end'])
            st.markdown(f'''
                        **Start:** {start}s **End:** {end}s 
                        
                        **Text:** {segment['text']}
                        ''')
    
    if transcript['text']:
        st.markdown('**Transcript:**' + transcript['text'])