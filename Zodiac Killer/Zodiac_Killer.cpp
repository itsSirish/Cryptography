#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

string encodeHelper(vector<vector<char>>& matrix, string input, int rowSize, int colSize) {
    string encoded_result = "";
    int i = 0, j = 0;
    for (int k = 0; k < rowSize; k++) {
        j = k;
        for (int l = 0; l < colSize; l++) {
            if (i == input.length()) {
                break;
            }
            matrix[l][j % rowSize] = input[i];
            j += 2;
            i++;
        }
    }
    for (int a = 0; a < colSize; a++) {
        for (int b = 0; b < rowSize; b++) {
            encoded_result += matrix[a][b];
        }
    }
    return encoded_result;
}

int main() {
    int rowSize;
    cin >> rowSize;
    string input;
    cin >> input;
    int colSize = ceil(input.length() / (double)rowSize);
    vector<vector<char>> matrix(colSize, vector<char>(rowSize, 'Z'));
    cout << encodeHelper(matrix, input, rowSize, colSize) << endl;
    return 0;
}
