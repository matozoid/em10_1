plugins {
    kotlin("multiplatform") version "2.4.20"
}

group = "em10"
version = "0.1.0"

kotlin {
    jvm {
        binaries {
            executable {
                mainClass.set("em10.cli.MainKt")
            }
        }
    }
    sourceSets {
        commonTest.dependencies {
            implementation(kotlin("test"))
        }
    }
}
