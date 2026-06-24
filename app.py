import streamlit as st
import os
import shutil

from src.pipeline import ClinicalPipeline
from src.pdf.pdf_reader import PDFReader

# Initialize components
pipeline = ClinicalPipeline()
pdf_reader = PDFReader()

# Page configuration
st.set_page_config(
    page_title="Clinical Narrative Reconstruction Agent",
    layout="wide"
)

st.title("🏥 Clinical Narrative Reconstruction Agent")

# Upload TXT and PDF files
uploaded_files = st.file_uploader(
    "Upload Medical Reports",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    # Clean temp folder
    temp_dir = "data/temp"

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    os.makedirs(temp_dir)

    st.success(
        f"{len(uploaded_files)} file(s) uploaded successfully!"
    )

    # Process uploaded files
    for uploaded_file in uploaded_files:

        file_extension = (
            uploaded_file.name
            .split(".")[-1]
            .lower()
        )

        # TXT FILE
        if file_extension == "txt":

            content = (
                uploaded_file.read()
                .decode("utf-8")
            )

        # PDF FILE
        elif file_extension == "pdf":

            temp_pdf = os.path.join(
                temp_dir,
                uploaded_file.name
            )

            with open(temp_pdf, "wb") as f:
                f.write(
                    uploaded_file.getbuffer()
                )

            content = pdf_reader.extract_text(
                temp_pdf
            )

            # Delete temporary PDF after extraction
            os.remove(temp_pdf)

        else:
            continue

        # Save extracted text
        txt_path = os.path.join(
            temp_dir,
            uploaded_file.name + ".txt"
        )

        with open(
            txt_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)

    # Show uploaded files
    st.subheader("📄 Uploaded Reports")

    for uploaded_file in uploaded_files:

        st.write(
            f"📄 {uploaded_file.name}"
        )

    # Run pipeline
    result = pipeline.process_folder(
        temp_dir
    )

    st.divider()

    # Summary Metrics
    st.subheader("📈 Patient Summary")

    colA, colB, colC = st.columns(3)

    colA.metric(
        "Reports Processed",
        len(result["reports"])
    )

    colB.metric(
        "Timeline Events",
        len(result["timeline"])
    )

    colC.metric(
        "Alerts",
        len(result["alerts"])
    )

    st.divider()

    # Main Dashboard
    col1, col2 = st.columns(2)

    # LEFT COLUMN
    with col1:

        st.subheader(
            "📊 Extracted Entities"
        )

        for report in result["reports"]:
            st.json(report)

        st.subheader("📅 Timeline")

        for event in result["timeline"]:

            st.write(
                f"📅 {event['date'].strftime('%d-%m-%Y')}"
            )

            st.write(
                "Diagnoses: " +
                ", ".join(event["diagnoses"])
            )

            st.write(
                "Medications: " +
                ", ".join(event["medications"])
            )

            st.write(
                f"Lab Results: {event['lab_results']}"
            )

            st.divider()

        # RIGHT COLUMN
        with col2:

            st.subheader(
                "📝 Clinical Narrative"
            )

            st.info(
                result["narrative"]
            )

            st.download_button(
                label="📥 Download Clinical Summary",
                data=result["narrative"],
                file_name="clinical_summary.txt",
                mime="text/plain"
            )

            st.subheader(
                "⚠ Clinical Alerts"
            )

            if result["alerts"]:

                for alert in result["alerts"]:

                    st.error(
                        alert["message"]
                    )

            else:

                st.success(
                    "No clinical conflicts detected."
                )