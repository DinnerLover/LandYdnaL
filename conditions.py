print(f" {'FINAL GRADING':_^80} ")
midterms = int(input ("Midterm score\t:"))
finals = int(input ("Finals score\t:"))
average = (midterms * 0.4) + (finals * 0.6)
print(f"Average score\t: {average}")
if(average == 100):
    print("Perfect!")