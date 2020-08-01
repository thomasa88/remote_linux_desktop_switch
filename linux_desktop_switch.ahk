#NoEnv

#Include Socket.ahk

;SetBatchLines, -1

^!Up::sendPacket(0)
^!Down::sendPacket(2)

sendPacket(direction) {
    UDP := new SocketUDP()
    UDP.Connect(["box", "48484"])
    len := 1
    VarSetCapacity(packet, len, 0x00)
    NumPut(direction, packet, 0, "UChar")
    UDP.Send(&packet, len)
}
