import matplotlib.pyplot as plt
import networkx as nx

def create_csma_persistent_flow():
    G = nx.DiGraph()
    
    # Define nodes for each persistence method
    nodes = {
        "Start": (0, 3),
        "Check Channel Idle (1-persistent)": (2, 3),
        "Channel Idle - Transmit (1-persistent)": (4, 4),
        "Channel Busy - Wait (1-persistent)": (4, 2),
        
        "Check Channel Idle (Non-persistent)": (6, 3),
        "Channel Idle - Transmit (Non-persistent)": (8, 4),
        "Channel Busy - Wait Randomly (Non-persistent)": (8, 2),
        
        "Check Channel Idle (p-persistent)": (10, 3),
        "Probability Condition Met - Transmit (p-persistent)": (12, 4),
        "Probability Condition Not Met - Wait Slot (p-persistent)": (12, 2),
        "Channel Busy - Back-Off (p-persistent)": (10, 1)
    }
    
    # Add nodes to the graph
    for node, pos in nodes.items():
        G.add_node(node, pos=pos)

    # Define edges for 1-persistent
    G.add_edges_from([
        ("Start", "Check Channel Idle (1-persistent)"),
        ("Check Channel Idle (1-persistent)", "Channel Idle - Transmit (1-persistent)"),
        ("Check Channel Idle (1-persistent)", "Channel Busy - Wait (1-persistent)"),
        ("Channel Busy - Wait (1-persistent)", "Check Channel Idle (1-persistent)")
    ])
    
    # Define edges for non-persistent
    G.add_edges_from([
        ("Start", "Check Channel Idle (Non-persistent)"),
        ("Check Channel Idle (Non-persistent)", "Channel Idle - Transmit (Non-persistent)"),
        ("Check Channel Idle (Non-persistent)", "Channel Busy - Wait Randomly (Non-persistent)"),
        ("Channel Busy - Wait Randomly (Non-persistent)", "Check Channel Idle (Non-persistent)")
    ])
    
    # Define edges for p-persistent
    G.add_edges_from([
        ("Start", "Check Channel Idle (p-persistent)"),
        ("Check Channel Idle (p-persistent)", "Probability Condition Met - Transmit (p-persistent)"),
        ("Check Channel Idle (p-persistent)", "Probability Condition Not Met - Wait Slot (p-persistent)"),
        ("Probability Condition Not Met - Wait Slot (p-persistent)", "Check Channel Idle (p-persistent)"),
        ("Check Channel Idle (p-persistent)", "Channel Busy - Back-Off (p-persistent)"),
        ("Channel Busy - Back-Off (p-persistent)", "Check Channel Idle (p-persistent)")
    ])
    
    # Get positions and draw
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)
    plt.title("CSMA Persistent Flow Diagram")
    plt.show()

create_csma_persistent_flow()
