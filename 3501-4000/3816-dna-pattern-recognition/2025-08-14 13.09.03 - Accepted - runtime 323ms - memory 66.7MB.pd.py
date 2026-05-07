import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    s=samples['dna_sequence']
    
    samples['has_start']=[1 if c.startswith("ATG") else 0 for c in s]

    samples['has_stop']=[1 if c.endswith("TAA") or c.endswith("TAG") or c.endswith("TGA") else 0 for c in s]

    samples['has_atat']=[1 if "ATAT" in c else 0 for c in s]

    samples['has_ggg']=[1 if "GGG" in c else 0 for c in s]


    return samples.sort_values('sample_id')