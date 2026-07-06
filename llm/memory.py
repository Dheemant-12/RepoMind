class ConversationMemory:

    def __init__(self):

        self.history = []

        self.last_function = None

    def update(self, question, answer, function_name=None):

        self.history.append({

            "question": question,

            "answer": answer

        })

        if function_name:

            self.last_function = function_name

    def resolve_question(self, question):

        question_lower = question.lower()

        if self.last_function:

            if "it" in question_lower:

                question = question.replace(
                    "it",
                    self.last_function
                )

                question = question.replace(
                    "It",
                    self.last_function
                )

        return question

    def clear(self):

        self.history.clear()

        self.last_function = None