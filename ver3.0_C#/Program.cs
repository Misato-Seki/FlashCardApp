using System;

class QuizProgram
{
    static void Main()
    {
        Console.WriteLine("Welcom to the Flashcard App!");

        // Create arrays to store questions and correct answers
        int numberOfQuestions = 10;
        string[] questions = new string[numberOfQuestions];
        string[] correctAnswer = new string[numberOfQuestions];

        // Populate arrays withe user input
        for(int i = 0; i < numberOfQuestions; i++)
        {
            Console.WriteLine("1. Register Flashcard 2. Quit");
            int userInput = int.Parse(Console.ReadLine());

            // 1. Register Flashcard
            if(userInput == 1)
            {
                // Get the question
                Console.Write("Question: ");
                questions[i] = Console.ReadLine();

                // Get the Answer
                Console.Write("Enter the correct answer: ");
                correctAnswer[i] = Console.ReadLine();
            }
            // 2. Quit
            else
            {
                break;
            }            
        }

        // Recode player's score
        int playerScore = 0;

        // Ask questions and show correct answers
        Console.WriteLine("\nLet's start the quiz!");
        for(int i = 0; i < numberOfQuestions; i++)
        {
            // Ask questions
            Console.WriteLine($"11Question {i + 1}: \n{questions[i]}");

            // Show answer or Quit
            Console.WriteLine("1. Show the answer 2. Quit");
            int userChoice = int.Parse(Console.ReadLine());

            // 1. Show the answer
            if(userChoice == 1)
            {
                Console.WriteLine($"Correct Answer: {correctAnswer[i]}");

                // Calculate the player's score
                Console.WriteLine("1. Correct 2. Wrong");
                int userInput = int.Parse(Console.ReadLine());

                // 1. Correct
                if(userInput == 1)
                {
                    Console.WriteLine("You got a point!");
                    playerScore++;
                }

                // 2. Wrong
                else
                {
                    Console.WriteLine("Good luck!");
                }
            }

            // 2. Quit
            else
            {
                break;
            }
        }

        Console.WriteLine("\nQuiz Completed!");
        Console.WriteLine($"Your score is {playerScore}/{numberOfQuestions}");
    }
}