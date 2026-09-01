## Leader Election Example  
This example demonstrates how to use the leader election library.

## Running
Run the following command in multiple separate terminals preferably an odd number. 
Each running process uses a unique identifier displayed when it starts to run.

- When a program runs, if a lock object already exists with the specified name, 
all candidates will start as followers. 
- If a lock object does not exist with the specified name then whichever candidate 
creates a lock object first will become the leader and the rest will be followers.
- The user will be prompted about the status of the candidates and transitions. 

### Command to run
```python example.py```

Now kill the existing leader. You will see from the terminal outputs that one of the
 remaining running processes will be elected as the new leader.
