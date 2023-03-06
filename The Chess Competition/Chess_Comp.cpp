#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

std::string decrypt_board(std::string matrix_str, int col1, int col2, std::string ciphertext) {
    int rows = 3;
    int cols = 10;
    std::vector<std::vector<char>> mat;
    int index = 0;
    matrix_str += "--";
    for (int i = 0; i < rows; i++) {
        mat.push_back(std::vector<char>());
        for (int j = 0; j < cols; j++) {
            if (i == 0) {
                if (j != col1 && j != col2) {
                    mat[i].push_back(matrix_str[index]);
                    index++;
                } else {
                    mat[i].push_back('-');
                }
            } else {
                mat[i].push_back(matrix_str[index]);
                index++;
            }
        }
    }

    std::unordered_map<int, char> char_map;

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (row == 0) {
                if (mat[row][col] != '-') {
                    char_map[col] = mat[row][col];
                }
            } else if (row == 1) {
                int key = std::stoi(std::to_string(col1) + std::to_string(col));
                char_map[key] = mat[row][col];
            } else {
                if (col == 8 || col == 9) {
                    break;
                }
                int key = std::stoi(std::to_string(col2) + std::to_string(col));
                char_map[key] = mat[row][col];
            }
        }
    }

    std::vector<std::string> codes;
    int i = 0;
    while (i < ciphertext.length()) {
        if (ciphertext[i] == std::to_string(col1)[0] || ciphertext[i] == std::to_string(col2)[0]) {
            codes.push_back(ciphertext.substr(i, 2));
            i += 2;
        } else {
            codes.push_back(ciphertext.substr(i, 1));
            i += 1;
        }
    }

    std::string answer;
    for (std::string code : codes) {
        answer += char_map[std::stoi(code)];
    }

    return answer;
}

int main() {
    std::string matrix_str, ciphertext;
    int col1, col2;

    std::getline(std::cin, matrix_str);
    std::cin >> col1 >> col2;
    std::cin.ignore();
    std::getline(std::cin, ciphertext);

    std::string plaintext = decrypt_board(matrix_str, col1, col2, ciphertext);
    std::cout << plaintext << std::endl;

    return 0;
}