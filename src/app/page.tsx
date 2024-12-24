import CustomTypeWriter from "@/components/custom/custom-type-writer";
import { MainForm } from "@/components/form/main-form";
import { ToggleTheme } from "@/components/theme/toggle-theme";

export default function Home() {
  
  return (
    <div className="flex flex-col w-full min-h-[80vh] items-center justify-center">
          <CustomTypeWriter/>
          <MainForm/>
          <ToggleTheme/>
    </div>
  );
}
