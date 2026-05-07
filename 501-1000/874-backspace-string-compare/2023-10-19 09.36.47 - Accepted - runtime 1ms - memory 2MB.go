func backspaceCompare(S string, T string) bool {
    stackS := make([]rune, 0)
    stackT := make([]rune, 0)

    for _, char := range S {
        if char == '#' {
            if len(stackS) > 0 {
                stackS = stackS[:len(stackS)-1]
            }
        } else {
            stackS = append(stackS, char)
        }
    }

    for _, char := range T {
        if char == '#' {
            if len(stackT) > 0 {
                stackT = stackT[:len(stackT)-1]
            }
        } else {
            stackT = append(stackT, char)
        }
    }

    return string(stackS) == string(stackT)    
}