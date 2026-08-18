"""Reference ranges used by the demo application.

These values are part of the project's educational rule set and are not a
substitute for laboratory-specific clinical reference intervals.
"""

BLOOD_TESTS = {
    'Hemoglobin': {
        'name': 'Hemoglobin',
        'units': 'g/dL',
        'ranges': {
            'male': {'min': 13.5, 'max': 17.5},
            'female': {'min': 12.0, 'max': 15.5}
        },
        'low': {
            'condition': 'Anemia, Blood loss, Chronic disease, Nutritional deficiency, Bone marrow disorder, Kidney disease',
            'symptoms': 'Fatigue, Weakness, Pale skin, Shortness of breath, Dizziness'
        },
        'high': {
            'condition': 'Dehydration, Polycythemia vera, Lung disease, High altitude adaptation',
            'symptoms': 'Headache, Dizziness, Flushed skin, Blurred vision, Itching'
        }
    },
    'RBC': {
        'name': 'Red Blood Cells',
        'units': 'million cells/μL',
        'ranges': {
            'male': {'min': 4.5, 'max': 5.9},
            'female': {'min': 4.0, 'max': 5.2}
        },
        'low': {
            'condition': 'Anemia, Bone marrow failure, Nutritional deficiency, Chronic inflammation, Hemolysis',
            'symptoms': 'Fatigue, Pale skin, Rapid heartbeat, Cold hands/feet'
        },
        'high': {
            'condition': 'Dehydration, Polycythemia vera, Hypoxia, Kidney tumor',
            'symptoms': 'Fatigue, Headache, Blurred vision, Itching (especially after shower)'
        }
    },
    'HCT': {
        'name': 'Hematocrit',
        'units': '%',
        'ranges': {
            'male': {'min': 40, 'max': 50},
            'female': {'min': 36, 'max': 46}
        },
        'low': {
            'condition': 'Anemia, Bleeding, Nutritional deficiency, Bone marrow disorder',
            'symptoms': 'Fatigue, Weakness, Pale skin, Shortness of breath'
        },
        'high': {
            'condition': 'Dehydration, Polycythemia vera, Chronic lung disease',
            'symptoms': 'Headache, Dizziness, Flushed skin, Vision problems'
        }
    },
    'MCV': {
        'name': 'Mean Corpuscular Volume',
        'units': 'fL',
        'ranges': {'min': 80, 'max': 100},
        'low': {
            'condition': 'Iron deficiency anemia, Thalassemia, Chronic disease',
            'symptoms': 'Fatigue, Pale skin, Brittle nails, Pica (craving ice/dirt)'
        },
        'high': {
            'condition': 'Vitamin B12 deficiency, Folate deficiency, Liver disease, Hypothyroidism',
            'symptoms': 'Fatigue, Diarrhea, Numbness/tingling, Balance problems'
        }
    },
    'MCH': {
        'name': 'Mean Corpuscular Hemoglobin',
        'units': 'pg',
        'ranges': {'min': 27, 'max': 33},
        'low': {
            'condition': 'Iron deficiency anemia, Thalassemia',
            'symptoms': 'Fatigue, Pale skin, Weakness, Shortness of breath'
        },
        'high': {
            'condition': 'Macrocytic anemia, Reticulocytosis',
            'symptoms': 'Fatigue, Pale skin, Diarrhea, Numbness in extremities'
        }
    },
    'MCHC': {
        'name': 'Mean Corpuscular Hemoglobin Concentration',
        'units': 'g/dL',
        'ranges': {'min': 32, 'max': 36},
        'low': {
            'condition': 'Iron deficiency anemia, Thalassemia',
            'symptoms': 'Fatigue, Pale skin, Brittle nails, Cold intolerance'
        },
        'high': {
            'condition': 'Hereditary spherocytosis, Hemoglobin C disease',
            'symptoms': 'Fatigue, Jaundice, Enlarged spleen, Gallstones'
        }
    },
    'RDW-CV': {
        'name': 'Red Cell Distribution Width (CV)',
        'units': '%',
        'ranges': {'min': 11.5, 'max': 14.5},
        'low': {
            'condition': 'Not clinically significant',
            'symptoms': 'None typically'
        },
        'high': {
            'condition': 'Iron deficiency anemia, Vitamin B12 deficiency, Hemoglobinopathy, Myelodysplasia',
            'symptoms': 'Varies by underlying condition (fatigue, weakness, pallor)'
        }
    },
    'RDW-SD': {
        'name': 'Red Cell Distribution Width (SD)',
        'units': 'fL',
        'ranges': {'min': 39, 'max': 46},
        'low': {
            'condition': 'Not clinically significant',
            'symptoms': 'None typically'
        },
        'high': {
            'condition': 'Iron deficiency anemia, Vitamin B12 deficiency, Hemoglobinopathy, Myelodysplasia',
            'symptoms': 'Varies by underlying condition (fatigue, weakness, pallor)'
        }
    },
    'WBC': {
        'name': 'White Blood Cells',
        'units': '×10³/μL',
        'ranges': {'min': 4.0, 'max': 11.0},
        'low': {
            'condition': 'Viral infection, Bone marrow disorder, Autoimmune disease, Severe infection',
            'symptoms': 'Frequent infections, Fever, Fatigue, Mouth sores'
        },
        'high': {
            'condition': 'Bacterial infection, Leukemia, Inflammation, Stress response',
            'symptoms': 'Fever, Pain, Fatigue, Night sweats (if leukemia)'
        }
    },
    'NEU%': {
        'name': 'Neutrophils',
        'units': '%',
        'ranges': {'min': 40, 'max': 70},
        'low': {
            'condition': 'Viral infection, Autoimmune disorder, Chemotherapy effect',
            'symptoms': 'Frequent infections, Fever, Mouth ulcers'
        },
        'high': {
            'condition': 'Bacterial infection, Acute inflammation, Steroid use',
            'symptoms': 'Fever, Pain, Redness/swelling at infection site'
        }
    },
    'LYM%': {
        'name': 'Lymphocytes',
        'units': '%',
        'ranges': {'min': 20, 'max': 40},
        'low': {
            'condition': 'HIV/AIDS, Immunosuppression, Radiation exposure',
            'symptoms': 'Frequent infections, Weight loss, Fatigue'
        },
        'high': {
            'condition': 'Viral infection, Chronic infection, Lymphoma',
            'symptoms': 'Swollen lymph nodes, Fever, Night sweats'
        }
    },
    'MON%': {
        'name': 'MON%',
        'units': '%',
        'ranges': {'min': 2, 'max': 10},
        'low': {
            'condition': '',
            'symptoms': ''
        },
        'high': {
            'condition': 'Chronic infection, Autoimmune disease, Myeloproliferative disorder',
            'symptoms': ''
        }
    },
    'EOS%': {
        'name': 'EOS%',
        'units': '%',
        'ranges': {'min': 0, 'max': 6},
        'low': {
            'condition': '',
            'symptoms': ''
        },
        'high': {
            'condition': 'Allergic disorder, Parasitic infection, Autoimmune disease',
            'symptoms': ''
        }
    },
    'BAS%': {
        'name': 'BAS%',
        'units': '%',
        'ranges': {'min': 0, 'max': 2},
        'low': {
            'condition': '',
            'symptoms': ''
        },
        'high': {
            'condition': 'Allergic reaction, Chronic inflammation, Myeloproliferative disorder',
            'symptoms': ''
        }
    },
    'LYM#': {
        'name': 'LYM#',
        'units': '×10³/μL',
        'ranges': {'min': 1.0, 'max': 4.0},
        'low': {
            'condition': 'HIV/AIDS, Immunosuppression',
            'symptoms': 'Frequent infections, Weight loss, Fatigue'
        },
        'high': {
            'condition': 'Viral infection, Lymphoma',
            'symptoms': 'Swollen lymph nodes, Fever, Night sweats'
        }
    },
    'GRA#': {
        'name': 'GRA#',
        'units': '×10³/μL',
        'ranges': {'min': 1.8, 'max': 7.0},
        'low': {
            'condition': 'Chemotherapy effect, Bone marrow failure',
            'symptoms': ''
        },
        'high': {
            'condition': 'Bacterial infection, Inflammation',
            'symptoms': ''
        }
    },
    'PLT': {
        'name': 'Platelets',
        'units': '×10³/μL',
        'ranges': {'min': 150, 'max': 450},
        'low': {
            'condition': 'Viral infection, Autoimmune disorder, Bone marrow disorder',
            'symptoms': 'Easy bruising, Prolonged bleeding, Petechiae (small red spots)'
        },
        'high': {
            'condition': 'Inflammation, Iron deficiency, Myeloproliferative disorder',
            'symptoms': 'Headache, Dizziness, Blood clots (in extreme cases)'
        }
    },
    'ESR': {
        'name': 'Erythrocyte Sedimentation Rate',
        'units': 'mm/hr',
        'ranges': {
            'male': {'min': 0, 'max': 15},
            'female': {'min': 0, 'max': 20}
        },
        'low': {
            'condition': 'Not clinically significant',
            'symptoms': 'None'
        },
        'high': {
            'condition': 'Inflammation, Infection, Autoimmune disease, Malignancy',
            'symptoms': 'Depends on underlying condition (joint pain, fever, fatigue)'
        }
    }
}

# Rule-based recommendations for common blood test abnormalities
# This dictionary contains conditions and their respective recommendations
