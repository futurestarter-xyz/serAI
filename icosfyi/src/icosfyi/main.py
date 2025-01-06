#!/usr/bin/env python
import sys
import warnings

from icosfyi.crew import Icosfyi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'platform_name': 'ICOs.fyi',
        'target_market': 'Crypto investors and Web3 enthusiasts',
        'primary_goal': 'User acquisition and platform growth'
    }
    Icosfyi().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'platform_name': 'ICOs.fyi',
        'target_market': 'Crypto investors and Web3 enthusiasts',
        'primary_goal': 'User acquisition and platform growth'
    }
    try:
        Icosfyi().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Icosfyi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'platform_name': 'ICOs.fyi',
        'target_market': 'Crypto investors and Web3 enthusiasts',
        'primary_goal': 'User acquisition and platform growth'
    }
    try:
        Icosfyi().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()