def question(question, answer):
    sc = input(question)
    while(sc is not answer): sc = input("Try Again\n"+question)
    print("Correct")
question(("What is 1 + 1? is it A) 0, B) 1, or C)2 "), "c")
question(("Who teaches all the computer science classes at Bradley? is it A) Mr. Delapina, B) Mr. Riely, or C) Mrs. Whitman "), "b")
question(("Who was the best copmputer science teacher that bradley ever had? Is it A) Mrs. Whitman, B) Mrs. White, or C) Mr. Riely "), "a")