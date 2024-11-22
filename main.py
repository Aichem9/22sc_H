import streamlit as st
import pandas as pd

# Load data
file_path = '22scapp.xlsx'
sheet_data = pd.read_excel(file_path, sheet_name='고등_현장적용')

# Title
st.title("과학실험 기구 점검 앱")

# Sidebar filter
st.sidebar.header("필터링 옵션")
importance_filter = st.sidebar.multiselect(
    "중요도 (필수/권장/확장)",
    options=sheet_data["필수/권장/확장"].unique(),
    default=sheet_data["필수/권장/확장"].unique()
)

area_filter = st.sidebar.multiselect(
    "영역 선택",
    options=sheet_data["영역"].unique(),
    default=sheet_data["영역"].unique()
)

# Apply filters
filtered_data = sheet_data[
    (sheet_data["필수/권장/확장"].isin(importance_filter)) &
    (sheet_data["영역"].isin(area_filter))
]

# Add checkbox for inspection
st.subheader("기구 점검 목록")
filtered_data["점검 완료"] = False
for index, row in filtered_data.iterrows():
    checked = st.checkbox(row["2022 개정 교구명"], key=index)
    filtered_data.at[index, "점검 완료"] = checked

# Save results button
if st.button("결과 저장"):
    save_path = "점검 결과.xlsx"
    filtered_data.to_excel(save_path, index=False)
    st.success(f"결과가 '{save_path}'로 저장되었습니다.")

# Display data
st.write("점검된 데이터:")
st.dataframe(filtered_data)
