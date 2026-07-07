class ContextBuilder:

    @staticmethod
    def build(question, context):

        route = context["route"]

        if route == "SEMANTIC":

            result = context["results"][0]

            return f"""
Question:
{question}

Relevant Function:
{result['function']}

Location:
{result['file']}

Similarity Distance:
{result['distance']}

Source Code:
{result['source']}
"""

        elif route == "GRAPH":

            graph = context["results"]

            return f"""
Question:
{question}

Target Function:
{graph['function']}

Direct Callers:
{graph['direct_callers']}

Affected Files:
{graph['affected_files']}

Risk:
{graph['risk']}
"""

        else:

            semantic = context["semantic"][0]
            graph = context["graph"]

            return f"""
Question:
{question}

Relevant Function:
{semantic['function']}

Location:
{semantic['file']}

Risk:
{graph['risk']}

Affected Files:
{graph['affected_files']}

Code:
{semantic['source']}
"""