import streamlit as st
import jd_analyzer

st.title("AI Career Assistant")
st.header("JD Analyzer")

user_input = st.text_area("Paste Job Description here")

if st.button("Analyze"):
    with st.spinner("Analyzing JD..."):
        res = jd_analyzer.analyze_jd(user_input)
    
        st.subheader("Analysis Results")
        st.metric("Role", res.role_title)                                   # type:ignore
        st.write("**Required Skills:**")
        for skill in res.required_skills:                                   # type:ignore
            st.write(f"  ✅ {skill}") 
            
        st.write("**Nice To Have Skills:**")               
        if res.nice_to_have:                                                # type:ignore
            for skill in res.nice_to_have:                                  # type:ignore
                st.write(f"  ⭐ {skill}")
        else:
            st.write("None mentioned")                      
        st.write(f"Experience: {res.experience_years or 'Not mentioned'}")  # type:ignore
        st.write(f"Location: {res.location or 'Not mentioned'}")            # type:ignore
        if res.match_recommendation.value == "apply":                       # type:ignore
            st.success("✅ Recommendation: APPLY")
        else:
            st.error("❌ Recommendation: SKIP")