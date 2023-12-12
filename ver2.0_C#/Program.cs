class QuizProgram
{
    static void Main()
    {
        //create questions
        string[] questions =
        {
            "dog",
            "cat",
            "rabbit"
        };

        //create answers
        string[] answeres =
        {
            "A. koira\nB. kissa\nC.kani",
            "A. koira\nB. kissa\nC.kani",
            "A. koira\nB. kissa\nC.kani"
        };

        //create correctAnsweres
        int[] correctAnswers ={0, 1, 2};

        //recod players score
        int playersScore = 0;

        //ask questions
        Console.WriteLine("Welcome to the Finnish flashcard app!");
        for(int i = 0; i < questions.Length; i++)
        {
            Console.WriteLine("Question " + (i + 1));
            Console.WriteLine(questions[i]);
            Console.WriteLine(answeres[i]);
            Console.Write("Please enter your answer ('A', 'B', or 'C'): ");
            string playersAnswer = Console.ReadLine();

            //validating answer
            if(string.Equals(playersAnswer, "A", StringComparison.OrdinalIgnoreCase) && correctAnswers[i] == 0)
            {
                playersScore++;
            }
            else if(string.Equals(playersAnswer, "B", StringComparison.OrdinalIgnoreCase) && correctAnswers[i] == 1)
            {
                playersScore++;
            }
            else if(string.Equals(playersAnswer, "C", StringComparison.OrdinalIgnoreCase) && correctAnswers[i] == 2)
            {
                playersScore++;
            }

            //print score out to users
            Console.WriteLine("Quiz Completed!");
            Console.WriteLine("Your score is " + playersScore + "/" + questions.Length);

        }

    }

}