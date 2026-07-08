import streamlit as st
import jd_analyzer
import resume_matcher
import interview_preparation

st.title("AI Career Assistant")

tab1, tab2, tab3 = st.tabs(["JD Analyzer", "Resume Matcher", "Interview Prep"])

with tab1:
    jd_input = st.text_area("Paste Job Description here", key="jd_tab1")
    if st.button("Analyze"):
        with st.spinner("Analyzing JD..."):
            res = jd_analyzer.analyze_jd(jd_input)
        
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
                
with tab2:
    jd_input = st.text_area("Paste Job Description here", key="jd_tab2")
    resume_input = st.text_area("Paste Your Resume here", key="resume_tab2")    
    if st.button("Match"):
        with st.spinner("Matching Resume with JD..."):
            res = resume_matcher.match_resume(resume_input, jd_input)
        
            st.subheader("Matching Results")
            st.write("**Matching Skills:**")
            for skill in res.matched_skills:                                   # type:ignore
                st.write(f"  ✅ {skill}") 
                
            st.write("**Gap Skills:**")               
            if res.gap_skills:                                                # type:ignore
                for skill in res.gap_skills:                                  # type:ignore
                    st.write(f"  ❌ {skill}")
            else:
                st.write("None mentioned")
            st.metric("Match Percentage", f"{res.match_percentage}%")  # type:ignore            
            if res.recommendation.value == "apply":                       # type:ignore
                st.success("✅ Recommendation: APPLY")
            else:
                st.error("❌ Recommendation: SKIP")
                
with tab3:
    resume_input = st.text_area("Paste Your Resume here", key="resume_tab3")    
    jd_input = st.text_area("Paste Job Description here", key="jd_tab3")
    if st.button("Generate Interview Prep"):
        with st.spinner("Generating Interview Prep Question & Answers..."):
            result = interview_preparation.generate_interview_prep(resume_input, jd_input)
            
            st.subheader("Interview Preparation Questions")
            
            for i, q in enumerate(result.questions, 1):
                with st.expander(f"Question {i}: {q.question}"):
                    st.write(f"Answer: {q.suggested_answer}")
                                       
            
    