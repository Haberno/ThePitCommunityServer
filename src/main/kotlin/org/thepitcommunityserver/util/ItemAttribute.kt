package org.thepitcommunityserver.util

import net.minecraft.server.v1_8_R3.NBTTagCompound
import net.minecraft.server.v1_8_R3.NBTTagList


fun attackDamageModifier(damage: Double): Pair<String, NBTTagList> {
    val modifierList = NBTTagList()
    val modifier = NBTTagCompound().apply {
        setString("AttributeName", "generic.attackDamage")
        setString("Name", "generic.attackDamage")
        setDouble("Amount", damage)
        setInt("Operation", 0)
        setInt("UUIDLeast", 894654)
        setInt("UUIDMost", 2872)
        setString("Slot", "mainhand")
    }
    modifierList.add(modifier)
    return "AttributeModifiers" to modifierList
}





