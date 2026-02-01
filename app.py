from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_llm_response(input_text: str, expert_type: str):
    """
    指定された専門家の種類に基づいてLLMからの回答を取得する関数。
    :input_text: ユーザーからの入力テキスト
    :expert_type: ラジオボタンで選択された専門家の種類
    :return: LLMからの回答
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_type == "歴史":
        system_message = SystemMessage(content="あなたは歴史の専門家です。専門外の質問が来たら丁寧に断ってください。")
    elif expert_type == "科学":
        system_message = SystemMessage(content="あなたは科学の専門家です。専門外の質問が来たら丁寧に断ってください。")
    else: # その他一般
        system_message = SystemMessage(content="あなたは一般的な知識を持つAIです。")
    
    # LLMからの応答を取得
    messages = [system_message, HumanMessage(content=input_text)] 
    response = llm(messages)
    return response.content

st.title("専門家への質問アプリ")

st.write("##### 動作モード1: 歴史に関する質問")
st.write("入力フォームに歴史に関する質問テキストを入力し、「実行」ボタンを押すことで回答が得られます。")
st.write("##### 動作モード2: 科学に関する質問")
st.write("入力フォームに科学に関する質問テキストを入力し、「実行」ボタンを押すことで回答が得られます。")
st.write("##### 動作モード3: その他一般の質問")
st.write("入力フォームに歴史や科学以外の質問テキストを入力し、「実行」ボタンを押すことで回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["歴史", "科学", "その他一般"]
)

st.divider()

input_message = st.text_input("質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "歴史":
        if input_message:
            result = get_llm_response(input_text=input_message, expert_type="歴史")
            st.write(f"質問の回答: **{result}**")
        else:
            st.write("質問を入力してから実行ボタンを押してください。")
    elif selected_item == "科学":
        if input_message:
            result = get_llm_response(input_text=input_message, expert_type="科学") 
            st.write(f"質問の回答: **{result}**")
        else:
            st.write("質問を入力してから実行ボタンを押してください。")
    else: # その他一般
        if input_message:
            result = get_llm_response(input_text=input_message, expert_type="その他一般") 
            st.write(f"質問の回答: **{result}**")
        else:
            st.write("質問を入力してから実行ボタンを押してください。")