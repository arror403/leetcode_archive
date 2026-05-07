func arrayStringsAreEqual(a []string, b []string) bool {
    return strings.Join(a, "") == strings.Join(b, "")
}