__declspec(dllexport) int add_many(int n){
    int s = 0;
    for(int i = 0; i < n; i++){
        // s = s + 1
        s += i;
    }
    return s;
}