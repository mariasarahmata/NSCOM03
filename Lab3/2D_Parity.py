import matplotlib.pyplot as plt

def add_2d_parity(data, rows, cols):
    """
    Creates a 2D parity matrix and adds row and column parity bits.
    """
    # Convert data into a 2D matrix of integers
    matrix = [[int(data[i * cols + j]) for j in range(cols)] for i in range(rows)]
    
    # Calculate row parity (add an extra column for parity bits)
    for row in matrix:
        row.append(sum(row) % 2)  # Even parity for the row
    
    # Calculate column parity (add an extra row for parity bits)
    col_parity = [(sum(matrix[i][j] for i in range(rows)) % 2) for j in range(cols)]
    col_parity.append(sum(col_parity) % 2)  # Even parity for the parity row
    
    # Add the column parity as the last row in the matrix
    matrix.append(col_parity)
    
    return matrix

def visualize_2d_parity(matrix):
    """
    Visualizes the 2D parity matrix using matplotlib to match the provided example.
    """
    rows, cols = len(matrix), len(matrix[0])
    fig, ax = plt.subplots(figsize=(8, 5))

    # Draw the data matrix with parity bits
    for i in range(rows):
        for j in range(cols):
            cell_color = 'yellow'
            text_color = 'black' if i < rows - 1 and j < cols - 1 else 'red'
            ax.text(j + 0.5, rows - i - 0.5, str(matrix[i][j]), 
                    fontsize=14, ha='center', va='center', color=text_color,
                    bbox=dict(facecolor=cell_color, edgecolor='black', boxstyle='round,pad=0.3'))
    
    # Label the row and column parities
    ax.text(cols - 0.5, -0.7, "Column parities", fontsize=12, ha='center', va='center', color='red')
    ax.text(cols + 0.5, rows / 2, "Row parities", fontsize=12, ha='center', va='center', color='red', rotation=90)

    # Draw lines to separate the data area from the parity bits
    ax.plot([cols - 1, cols - 1], [0, rows], 'k-', lw=2)  # Vertical line
    ax.plot([0, cols], [1, 1], 'k-', lw=2)  # Horizontal line

    # Set axis limits and remove axes for a clean look
    ax.set_xlim(0, cols)
    ax.set_ylim(-1, rows)
    ax.axis('off')
    plt.title("2D Parity Check Matrix with Row and Column Parities")
    plt.tight_layout()
    plt.show()

# Example usage:
data = "11001111011101011100101010010101010" 
rows, cols = 4, 7

# Create the 2D parity matrix
parity_matrix = add_2d_parity(data, rows, cols)

# Visualize the 2D parity matrix
visualize_2d_parity(parity_matrix)
