import React from 'react';
import { Drawer, DrawerTrigger, DrawerContent, DrawerHeader, DrawerTitle, DrawerClose } from '../ui/drawer'; // Assuming these components are custom-built or from a library
import { Button } from '../ui/button';
import { Separator } from '../ui/separator';
import Image from 'next/image';
import Link from 'next/link';
import { X, ExternalLink } from 'lucide-react'; 

type inforDrawerProps = {
  triggerText?:"Show more information";
  title?:string;
  imageSrc?:string;
  imageAlt?:string;
  metadata?: {
    born?: string,
    died?: string,
    era?: string,
  }
  biographyText?: string;
  biographyLink?: string;
  videoUrl?: string;
}

const InfoDrawer = ({
  triggerText = "Show more information",
  title,
  imageSrc,
  metadata,
  imageAlt,
  biographyText,
  biographyLink,
  videoUrl,
}:inforDrawerProps) => {
  return (
    <Drawer>
      <DrawerTrigger className="text-muted-foreground text-sm underline hover:text-white/75 duration-200 mt-4">
        {triggerText}
      </DrawerTrigger>
      <DrawerContent className="min-h-[75%] px-24">
        <DrawerHeader>
          <DrawerTitle>{title}</DrawerTitle>
        </DrawerHeader>
        <DrawerClose className="absolute right-24 top-4">
          <Button variant="ghost">
            <X />
          </Button>
        </DrawerClose>

        <div className="size-full flex gap-6 mt-8">
          {/* Image Section */}
          <div className="w-1/5 aspect-[1/1.21] rounded-xl bg-white overflow-hidden">
            <Image src={imageSrc || ""} width={1000} height={1000} alt={imageAlt || "image of"} />
          </div>

          {/* Metadata and Biography Section */}
          <div className="w-2/5">
            {metadata && Object.entries(metadata).map(([key, value]) => (
              <p key={key} className="text-black/95 dark:text-white/95">
                <span className="min-w-12 inline-block capitalize">{key}:</span>
                <span className="text-muted-foreground">{value}</span>
              </p>
            ))}
            <Separator className="my-4" />
            <div>
              <p>
                <span className="text-muted-foreground">{biographyText}</span>
                {biographyLink && (
                  <Link
                    href={biographyLink}
                    target="_blank"
                    className="text-blue-400"
                  >
                    <ExternalLink className="w-4 pb-1 ml-1 inline" />
                  </Link>
                )}
              </p>
            </div>
          </div>

          {/* Video Section */}
          {videoUrl && (
            <div className="w-2/5 rounded-xl">
              <iframe
                src={videoUrl}
                allowFullScreen
                className="w-full aspect-video"
              ></iframe>
            </div>
          )}
        </div>
      </DrawerContent>
    </Drawer>
  );
};

export default InfoDrawer;
