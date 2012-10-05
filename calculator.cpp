#include <iostream>
using namespace std;

int get_sum() {
    int sum = 0;
    int count;
    cin >> count;
    while(count--) {
        int num;
        cin >> num;
        sum += num;
    }
    return sum;
}

int get_product() {
    int product = 1;
    int count;
    cin >> count;
    while(count--) {
        int num;
        cin >> num;
        product *= num;
    }
    return product;
}

int main() {
    string cmd;
    while(true) {
        cin >> cmd;

        if (cmd == "exit") {
            break;
        } else if (cmd == "sum") {
            cout << get_sum() << endl;
        } else if (cmd == "product") {
            cout << get_product() << endl;
        } else {
            cerr << "unknow command: " + cmd << endl;
        }

    }
    return 0;
}
